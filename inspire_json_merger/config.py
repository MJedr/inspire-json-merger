# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014-2017 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from __future__ import absolute_import, division, print_function

from json_merger.config import DictMergerOps as D, UnifierOps as U

from inspire_json_merger.utils import PRE_FILTERS
from .comparators import COMPARATORS

"""
This module provides different sets of rules that `inspire_json_merge`
"""


class MergerConfigurationOperations(object):
    default_dict_merge_op = D.FALLBACK_KEEP_UPDATE
    default_list_merge_op = U.KEEP_ONLY_UPDATE_ENTITIES
    conflict_filters = None
    comparators = None
    pre_filters = None
    list_dict_ops = None
    list_merge_ops = None


class ArxivOnArxivOperations(MergerConfigurationOperations):
    # We an always default to KEEP_UPDATE_AND_'HEAD_ENTITIES_HEAD_FIRST so
    # this is less verbose.
    comparators = COMPARATORS
    pre_filters = PRE_FILTERS
    conflict_filters = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'curated',
        'deleted',
        'deleted_records',
        'documents',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'figures',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'record_affiliations',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'related_records',
        'report_numbers',
        'self',
        'succeeding_entry',
        'texkeys',
        'thesis_info',
        'thesis_info.institutions',
        'title_translations',
        'titles',
        'urls',
        'withdrawn',
    ]

    list_merge_ops = {
        '_collections': U.KEEP_ONLY_HEAD_ENTITIES,
        '_desy_bookkeeping': U.KEEP_ONLY_HEAD_ENTITIES,
        '_files': U.KEEP_ONLY_UPDATE_ENTITIES,
        '_private_notes': U.KEEP_ONLY_HEAD_ENTITIES,
        'abstracts': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'accelerator_experiments': U.KEEP_ONLY_HEAD_ENTITIES,
        'arxiv_eprints': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.affiliations': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.alternative_names': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.credit_roles':
            U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.emails': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.full_name': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.ids': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.inspire_roles': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.raw_affiliations': U.KEEP_ONLY_UPDATE_ENTITIES,
        'book_series': U.KEEP_ONLY_HEAD_ENTITIES,
        'collaborations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'copyright': U.KEEP_ONLY_UPDATE_ENTITIES,
        'corporate_author': U.KEEP_ONLY_UPDATE_ENTITIES,
        'deleted_records': U.KEEP_ONLY_HEAD_ENTITIES,
        'documents': U.KEEP_ONLY_UPDATE_ENTITIES,
        'document_type': U.KEEP_ONLY_UPDATE_ENTITIES,
        'dois': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'editions': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'energy_ranges': U.KEEP_ONLY_UPDATE_ENTITIES,
        'external_system_identifiers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'figures': U.KEEP_ONLY_UPDATE_ENTITIES,
        'funding_info': U.KEEP_ONLY_HEAD_ENTITIES,
        'inspire_categories': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'isbns': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'keywords': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'languages': U.KEEP_ONLY_UPDATE_ENTITIES,
        'license': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'persistent_identifiers': U.KEEP_ONLY_HEAD_ENTITIES,
        'public_notes': U.KEEP_ONLY_UPDATE_ENTITIES,
        'publication_info': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'publication_type': U.KEEP_ONLY_UPDATE_ENTITIES,
        'record_affiliations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'related_records': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.raw_refs': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.authors': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.reference.book_series': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.collaboration': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.dois': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.misc': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.persistent_identifiers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.report_numbers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.urls': U.KEEP_ONLY_UPDATE_ENTITIES,
        'report_numbers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'texkeys': U.KEEP_ONLY_HEAD_ENTITIES,
        'thesis_info.institutions': U.KEEP_ONLY_UPDATE_ENTITIES,
        'title_translations': U.KEEP_ONLY_HEAD_ENTITIES,
        'titles': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'urls': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST
    }

    list_dict_ops = {
        '$schema': D.FALLBACK_KEEP_HEAD,
        '_desy_bookkeeping': D.FALLBACK_KEEP_HEAD,
        '_export_to': D.FALLBACK_KEEP_HEAD,
        '_private_notes': D.FALLBACK_KEEP_HEAD,
        'accelerator_experiments': D.FALLBACK_KEEP_HEAD,
        'acquisition_source': D.FALLBACK_KEEP_HEAD,
        'authors': D.FALLBACK_KEEP_HEAD,
        'authors.affiliations': D.FALLBACK_KEEP_HEAD,
        'authors.curated_relation': D.FALLBACK_KEEP_HEAD,
        'authors.full_name': D.keep_longest,
        'authors.ids': D.FALLBACK_KEEP_HEAD,
        'authors.inspire_roles': D.FALLBACK_KEEP_HEAD,
        'authors.record': D.FALLBACK_KEEP_HEAD,
        'authors.raw_affiliations': D.FALLBACK_KEEP_UPDATE,
        'authors.signature_block': D.FALLBACK_KEEP_UPDATE,
        'authors.uuid': D.FALLBACK_KEEP_UPDATE,
        'book_series': D.FALLBACK_KEEP_HEAD,
        'control_number': D.FALLBACK_KEEP_HEAD,
        'curated': D.FALLBACK_KEEP_HEAD,
        'deleted': D.FALLBACK_KEEP_HEAD,
        'deleted_records': D.FALLBACK_KEEP_HEAD,
        'funding_info': D.FALLBACK_KEEP_HEAD,
        'legacy_creation_date': D.FALLBACK_KEEP_HEAD,
        'new_record': D.FALLBACK_KEEP_HEAD,
        'persistent_identifiers': D.FALLBACK_KEEP_HEAD,
        'preprint_date': D.FALLBACK_KEEP_HEAD,
        'references': D.FALLBACK_KEEP_UPDATE,
        'references.reference': D.FALLBACK_KEEP_HEAD,
        'references.reference.arxiv_eprint': D.FALLBACK_KEEP_UPDATE,
        'references.reference.authors': D.FALLBACK_KEEP_UPDATE,
        'references.reference.book_series': D.FALLBACK_KEEP_UPDATE,
        'references.reference.document_type': D.FALLBACK_KEEP_UPDATE,
        'references.reference.dois': D.FALLBACK_KEEP_UPDATE,
        'references.reference.imprint': D.FALLBACK_KEEP_UPDATE,
        'references.reference.isbn': D.FALLBACK_KEEP_UPDATE,
        'references.reference.label': D.FALLBACK_KEEP_UPDATE,
        'references.reference.persistent_identifiers': D.FALLBACK_KEEP_UPDATE,
        'references.reference.report_number': D.FALLBACK_KEEP_UPDATE,
        'references.reference.texkey': D.FALLBACK_KEEP_UPDATE,
        'references.reference.title': D.FALLBACK_KEEP_UPDATE,
        'references.reference.urls': D.FALLBACK_KEEP_UPDATE,
        'self': D.FALLBACK_KEEP_HEAD,
        'succeeding_entry': D.FALLBACK_KEEP_HEAD,
        'texkeys': D.FALLBACK_KEEP_HEAD,
        'thesis_info.institutions': D.FALLBACK_KEEP_HEAD,
        'title_translations': D.FALLBACK_KEEP_HEAD,
        'urls': D.FALLBACK_KEEP_HEAD,
    }


class ArxivOnPublisherOperations(MergerConfigurationOperations):
    comparators = COMPARATORS
    pre_filters = PRE_FILTERS
    default_dict_merge_op = D.FALLBACK_KEEP_HEAD
    default_list_merge_op = U.KEEP_ONLY_HEAD_ENTITIES
    conflict_filters = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'curated',
        'deleted',
        'deleted_records',
        'documents',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'figures',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'record_affiliations',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'related_records',
        'report_numbers',
        'self',
        'succeeding_entry',
        'texkeys',
        'thesis_info',
        'thesis_info.institutions',
        'title_translations',
        'titles',
        'urls',
        'withdrawn',
    ]
    list_merge_ops = {
        'abstracts': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'arxiv_eprints': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.raw_affiliations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'copyright': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'documents': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'dois': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'external_system_identifiers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'figures': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'license': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'titles': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'public_notes': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'report_numbers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.raw_refs': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
    }
    list_dict_ops = {
        'authors.full_name': D.keep_longest
    }


class ManualMergeOperations(MergerConfigurationOperations):
    default_dict_merge_op = D.FALLBACK_KEEP_HEAD
    default_list_merge_op = U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST
    comparators = COMPARATORS
    pre_filters = []  # don't delete files with the same source
    conflict_filters = [
        '_collections',
        '_desy_bookkeeping',
        '_files',
        'acquisition_source',
        'control_number',
        'self',
    ]
    list_merge_ops = {}
    list_dict_ops = {
        'authors.full_name': D.keep_longest,
    }


class PublisherOnArxivOperations(MergerConfigurationOperations):
    comparators = COMPARATORS
    pre_filters = PRE_FILTERS
    conflict_filters = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'curated',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'deleted',
        'deleted_records',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'report_numbers',
        'self',
        'succeeding_entry',
        'texkeys',
        'thesis_info',
        'thesis_info.institutions',
        'title_translations',
        'titles',
        'urls',
        'withdrawn',
        'related_records',
        'record_affiliations',
    ]

    list_merge_ops = {
        '_collections': U.KEEP_ONLY_HEAD_ENTITIES,
        '_desy_bookkeeping': U.KEEP_ONLY_HEAD_ENTITIES,
        '_files': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        '_private_notes': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'abstracts': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'accelerator_experiments': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'arxiv_eprints': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.affiliations': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.alternative_names': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.credit_roles': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.emails': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'authors.ids': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'authors.raw_affiliations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'book_series': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'collaborations': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'copyright': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'corporate_author': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'deleted_records': U.KEEP_ONLY_HEAD_ENTITIES,
        'documents': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'document_type': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'dois': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'editions': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'energy_ranges': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'external_system_identifiers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'figures': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'funding_info': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'imprints': U.KEEP_ONLY_UPDATE_ENTITIES,
        'inspire_categories': U.KEEP_ONLY_HEAD_ENTITIES,
        'isbns': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'keywords': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'languages': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'license': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'persistent_identifiers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'public_notes': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'publication_info': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'publication_type': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'record_affiliations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'related_records': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.raw_refs': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'references.reference.authors': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.reference.book_series': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.collaboration': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.dois': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.misc': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.persistent_identifiers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.report_numbers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.urls': U.KEEP_ONLY_UPDATE_ENTITIES,
        'report_numbers': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'texkeys': U.KEEP_ONLY_HEAD_ENTITIES,
        'thesis_info.institutions': U.KEEP_ONLY_UPDATE_ENTITIES,
        'title_translations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'titles': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'urls': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST
    }

    list_dict_ops = {
        '$schema': D.FALLBACK_KEEP_HEAD,
        '_desy_bookkeeping': D.FALLBACK_KEEP_HEAD,
        '_export_to': D.FALLBACK_KEEP_HEAD,
        'abstracts': D.FALLBACK_KEEP_UPDATE,
        'accelerator_experiments': D.FALLBACK_KEEP_UPDATE,
        'acquisition_source': D.FALLBACK_KEEP_UPDATE,
        'arxiv_eprints': D.FALLBACK_KEEP_HEAD,
        'authors': D.FALLBACK_KEEP_HEAD,
        'authors.affiliations': D.FALLBACK_KEEP_HEAD,
        'authors.alternative_names': D.FALLBACK_KEEP_UPDATE,
        'authors.credit_roles': D.FALLBACK_KEEP_UPDATE,
        'authors.curated_relation': D.FALLBACK_KEEP_UPDATE,
        'authors.full_name': D.keep_longest,
        'authors.ids': D.FALLBACK_KEEP_HEAD,
        'authors.inspire_roles': D.FALLBACK_KEEP_HEAD,
        'authors.raw_affiliations': D.FALLBACK_KEEP_UPDATE,
        'authors.record': D.FALLBACK_KEEP_HEAD,
        'authors.signature_block': D.FALLBACK_KEEP_UPDATE,
        'authors.uuid': D.FALLBACK_KEEP_UPDATE,
        'book_series': D.FALLBACK_KEEP_UPDATE,
        'citeable': D.FALLBACK_KEEP_UPDATE,
        'collaborations': D.FALLBACK_KEEP_UPDATE,
        'control_number': D.FALLBACK_KEEP_HEAD,
        'copyright': D.FALLBACK_KEEP_UPDATE,
        'core': D.FALLBACK_KEEP_UPDATE,
        'corporate_author': D.FALLBACK_KEEP_UPDATE,
        'curated': D.FALLBACK_KEEP_HEAD,
        'deleted': D.FALLBACK_KEEP_HEAD,
        'deleted_records': D.FALLBACK_KEEP_HEAD,
        'editions': D.FALLBACK_KEEP_HEAD,
        'funding_info': D.FALLBACK_KEEP_UPDATE,
        'inspire_categories': D.FALLBACK_KEEP_HEAD,
        'isbns': D.FALLBACK_KEEP_HEAD,
        'preprint_date': D.FALLBACK_KEEP_HEAD,
        'publication_info': D.FALLBACK_KEEP_UPDATE,
        'refereed': D.FALLBACK_KEEP_UPDATE,
        'references': D.FALLBACK_KEEP_UPDATE,
        'references.reference': D.FALLBACK_KEEP_HEAD,
        'references.reference.arxiv_eprint': D.FALLBACK_KEEP_UPDATE,
        'references.reference.authors': D.FALLBACK_KEEP_UPDATE,
        'references.reference.book_series': D.FALLBACK_KEEP_UPDATE,
        'references.reference.document_type': D.FALLBACK_KEEP_UPDATE,
        'references.reference.dois': D.FALLBACK_KEEP_UPDATE,
        'references.reference.imprint': D.FALLBACK_KEEP_UPDATE,
        'references.reference.isbn': D.FALLBACK_KEEP_UPDATE,
        'references.reference.label': D.FALLBACK_KEEP_UPDATE,
        'references.reference.persistent_identifiers': D.FALLBACK_KEEP_UPDATE,
        'references.reference.publication_info': D.FALLBACK_KEEP_UPDATE,
        'references.reference.report_number': D.FALLBACK_KEEP_UPDATE,
        'references.reference.texkey': D.FALLBACK_KEEP_HEAD,
        'references.reference.title': D.FALLBACK_KEEP_UPDATE,
        'references.reference.urls': D.FALLBACK_KEEP_UPDATE,
        'report_numbers': D.FALLBACK_KEEP_HEAD,
        'self': D.FALLBACK_KEEP_HEAD,
        'succeeding_entry': D.FALLBACK_KEEP_HEAD,
        'texkeys': D.FALLBACK_KEEP_HEAD,
        'thesis_info.institutions': D.FALLBACK_KEEP_UPDATE,
        'title_translations': D.FALLBACK_KEEP_HEAD,
        'urls': D.FALLBACK_KEEP_HEAD
    }


class PublisherOnPublisherOperations(MergerConfigurationOperations):
    # We an always default to KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST so
    # this is less verbose.
    comparators = COMPARATORS
    pre_filters = PRE_FILTERS
    conflict_filters = [
        '_collections',
        '_files',
        'abstracts',
        'acquisition_source',
        'arxiv_eprints',
        'authors',
        'authors.affiliations',
        'authors.alternative_names',
        'authors.credit_roles',
        'authors.emails',
        'authors.full_name',
        'authors.raw_affiliations',
        'authors.record',
        'authors.signature_block',
        'authors.uuid',
        'authors.book_series',
        'authors.citeable',
        'authors.collaborations',
        'control_number',
        'copyright',
        'core',
        'corporate_author',
        'curated',
        'deleted',
        'deleted_records',
        'dois',
        'editions',
        'energy_ranges',
        'external_system_identifiers',
        'funding_info',
        'imprints',
        'inspire_categories',
        'isbns',
        'keywords',
        'languages',
        'legacy_creation_date',
        'license',
        'new_record',
        'number_of_pages',
        'persistent_identifiers',
        'preprint_date',
        'public_notes',
        'publication_info',
        'publication_type',
        'refereed',
        'references',
        'references.curated_relation',
        'references.raw_refs',
        'references.record',
        'references.reference',
        'references.reference.arxiv_eprint',
        'references.reference.authors',
        'references.reference.book_series',
        'references.reference.collaboration',
        'references.reference.document_type',
        'references.reference.dois',
        'references.reference.imprint',
        'references.reference.isbn',
        'references.reference.label',
        'references.reference.misc',
        'references.reference.persistent_identifiers',
        'references.reference.publication_info',
        'references.reference.report_number',
        'references.reference.texkey',
        'references.reference.title',
        'references.reference.urls',
        'report_numbers',
        'self',
        'succeeding_entry',
        'texkeys',
        'thesis_info',
        'thesis_info.institutions',
        'title_translations',
        'titles',
        'urls',
        'withdrawn',
        'related_records',
        'record_affiliations',
    ]

    list_merge_ops = {
        '_collections': U.KEEP_ONLY_HEAD_ENTITIES,
        '_desy_bookkeeping': U.KEEP_ONLY_HEAD_ENTITIES,
        '_files': U.KEEP_ONLY_UPDATE_ENTITIES,
        '_private_notes': U.KEEP_ONLY_HEAD_ENTITIES,
        'abstracts': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'accelerator_experiments': U.KEEP_ONLY_HEAD_ENTITIES,
        'arxiv_eprints': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.affiliations': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.alternative_names': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.credit_roles': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'authors.emails': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'authors.full_name': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.ids': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.inspire_roles': U.KEEP_ONLY_HEAD_ENTITIES,
        'authors.raw_affiliations': U.KEEP_ONLY_UPDATE_ENTITIES,
        'book_series': U.KEEP_ONLY_HEAD_ENTITIES,
        'collaborations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'copyright': U.KEEP_ONLY_UPDATE_ENTITIES,
        'corporate_author': U.KEEP_ONLY_UPDATE_ENTITIES,
        'deleted_records': U.KEEP_ONLY_HEAD_ENTITIES,
        'document_type': U.KEEP_ONLY_UPDATE_ENTITIES,
        'documents': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'dois': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'editions': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'energy_ranges': U.KEEP_ONLY_UPDATE_ENTITIES,
        'external_system_identifiers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'figures': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'funding_info': U.KEEP_ONLY_HEAD_ENTITIES,
        'inspire_categories': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'isbns': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'keywords': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'languages': U.KEEP_ONLY_UPDATE_ENTITIES,
        'license': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST,
        'persistent_identifiers': U.KEEP_ONLY_HEAD_ENTITIES,
        'public_notes': U.KEEP_ONLY_UPDATE_ENTITIES,
        'publication_info': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'publication_type': U.KEEP_ONLY_UPDATE_ENTITIES,
        'record_affiliations': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'related_records': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.raw_refs': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.authors': U.KEEP_UPDATE_ENTITIES_CONFLICT_ON_HEAD_DELETE,
        'references.reference.book_series': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.collaboration': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.dois': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.misc': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.persistent_identifiers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'references.reference.report_numbers': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'references.reference.urls': U.KEEP_ONLY_UPDATE_ENTITIES,
        'report_numbers': U.KEEP_ONLY_UPDATE_ENTITIES,
        'texkeys': U.KEEP_ONLY_HEAD_ENTITIES,
        'thesis_info.institutions': U.KEEP_ONLY_UPDATE_ENTITIES,
        'title_translations': U.KEEP_ONLY_HEAD_ENTITIES,
        'titles': U.KEEP_UPDATE_AND_HEAD_ENTITIES_HEAD_FIRST,
        'urls': U.KEEP_UPDATE_AND_HEAD_ENTITIES_UPDATE_FIRST
    }
    list_dict_ops = {
        '$schema': D.FALLBACK_KEEP_HEAD,
        '_desy_bookkeeping': D.FALLBACK_KEEP_HEAD,
        '_export_to': D.FALLBACK_KEEP_HEAD,
        '_private_notes': D.FALLBACK_KEEP_HEAD,
        'accelerator_experiments': D.FALLBACK_KEEP_HEAD,
        'acquisition_source': D.FALLBACK_KEEP_HEAD,
        'authors': D.FALLBACK_KEEP_HEAD,
        'authors.affiliations': D.FALLBACK_KEEP_HEAD,
        'authors.curated_relation': D.FALLBACK_KEEP_HEAD,
        'authors.full_name': D.keep_longest,
        'authors.ids': D.FALLBACK_KEEP_HEAD,
        'authors.inspire_roles': D.FALLBACK_KEEP_HEAD,
        'authors.record': D.FALLBACK_KEEP_HEAD,
        'authors.raw_affiliations': D.FALLBACK_KEEP_UPDATE,
        'authors.signature_block': D.FALLBACK_KEEP_UPDATE,
        'authors.uuid': D.FALLBACK_KEEP_UPDATE,
        'book_series': D.FALLBACK_KEEP_HEAD,
        'control_number': D.FALLBACK_KEEP_HEAD,
        'curated': D.FALLBACK_KEEP_HEAD,
        'deleted': D.FALLBACK_KEEP_HEAD,
        'deleted_records': D.FALLBACK_KEEP_HEAD,
        'funding_info': D.FALLBACK_KEEP_HEAD,
        'legacy_creation_date': D.FALLBACK_KEEP_HEAD,
        'new_record': D.FALLBACK_KEEP_HEAD,
        'persistent_identifiers': D.FALLBACK_KEEP_HEAD,
        'preprint_date': D.FALLBACK_KEEP_HEAD,
        'references': D.FALLBACK_KEEP_UPDATE,
        'references.reference': D.FALLBACK_KEEP_HEAD,
        'references.reference.arxiv_eprint': D.FALLBACK_KEEP_UPDATE,
        'references.reference.authors': D.FALLBACK_KEEP_UPDATE,
        'references.reference.book_series': D.FALLBACK_KEEP_UPDATE,
        'references.reference.document_type': D.FALLBACK_KEEP_UPDATE,
        'references.reference.dois': D.FALLBACK_KEEP_UPDATE,
        'references.reference.imprint': D.FALLBACK_KEEP_UPDATE,
        'references.reference.isbn': D.FALLBACK_KEEP_UPDATE,
        'references.reference.label': D.FALLBACK_KEEP_UPDATE,
        'references.reference.persistent_identifiers': D.FALLBACK_KEEP_UPDATE,
        'references.reference.report_number': D.FALLBACK_KEEP_UPDATE,
        'references.reference.texkey': D.FALLBACK_KEEP_UPDATE,
        'references.reference.title': D.FALLBACK_KEEP_UPDATE,
        'references.reference.urls': D.FALLBACK_KEEP_UPDATE,
        'self': D.FALLBACK_KEEP_HEAD,
        'succeeding_entry': D.FALLBACK_KEEP_HEAD,
        'texkeys': D.FALLBACK_KEEP_HEAD,
        'thesis_info.institutions': D.FALLBACK_KEEP_HEAD,
        'title_translations': D.FALLBACK_KEEP_HEAD,
        'urls': D.FALLBACK_KEEP_HEAD,
    }
